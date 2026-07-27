import os
import re
import shutil
import stat
import yaml
import markdown

WORKSPACE = r"c:\Users\gswr\OneDrive\GitHub\camera.github.io-imagine\IMAGINE"
SITE_DIR = os.path.join(WORKSPACE, "_site", "IMAGINE")

def load_yaml(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def read_file_with_front_matter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    front_matter = {}
    body = content
    
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        body = match.group(2)
        try:
            front_matter = yaml.safe_load(yaml_content) or {}
        except Exception as e:
            print(f"Error parsing front matter in {filepath}: {e}")
            
    return front_matter, body

def render_markdown(text):
    if not text:
        return ""
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'nl2br'])

def slugify(title):
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s\-]', '', s)
    s = re.sub(r'[\s\-]+', '-', s)
    return s

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

class PreviewBuilder:
    def __init__(self):
        self.config = load_yaml(os.path.join(WORKSPACE, "_config.yml")) or {}
        self.baseurl = self.config.get("baseurl", "")
        self.site_data = {
            "title": self.config.get("title", "IMAGINE"),
            "description": self.config.get("description", ""),
            "baseurl": self.baseurl,
            "data": {
                "people": load_yaml(os.path.join(WORKSPACE, "_data", "people.yml")),
                "institutions": load_yaml(os.path.join(WORKSPACE, "_data", "institutions.yml"))
            },
            "scanners": [],
            "components": [],
            "events": []
        }
        
        self.layouts = {}
        self.includes = {}
        
    def load_layouts_and_includes(self):
        layouts_dir = os.path.join(WORKSPACE, "_layouts")
        if os.path.exists(layouts_dir):
            for name in os.listdir(layouts_dir):
                if name.endswith(".html"):
                    layout_name = name[:-5]
                    _, body = read_file_with_front_matter(os.path.join(layouts_dir, name))
                    self.layouts[layout_name] = body
                    
        includes_dir = os.path.join(WORKSPACE, "_includes")
        if os.path.exists(includes_dir):
            for name in os.listdir(includes_dir):
                if name.endswith(".html"):
                    include_name = name[:-5]
                    with open(os.path.join(includes_dir, name), 'r', encoding='utf-8') as f:
                        self.includes[include_name] = f.read()

    def load_collections(self):
        scanners_dir = os.path.join(WORKSPACE, "_scanners")
        if os.path.exists(scanners_dir):
            for name in os.listdir(scanners_dir):
                if name.endswith(".md") or name.endswith(".html"):
                    fm, body = read_file_with_front_matter(os.path.join(scanners_dir, name))
                    fm["content"] = render_markdown(body)
                    fm["source_body"] = body
                    fm["source_path"] = os.path.join(scanners_dir, name)
                    fm["url"] = f"{self.baseurl}/scanners/{name[:-3]}/"
                    self.site_data["scanners"].append(fm)
                    
        events_dir = os.path.join(WORKSPACE, "_events")
        if os.path.exists(events_dir):
            for name in os.listdir(events_dir):
                if name.endswith(".md") or name.endswith(".html"):
                    fm, body = read_file_with_front_matter(os.path.join(events_dir, name))
                    fm["content"] = render_markdown(body)
                    fm["source_body"] = body
                    fm["source_path"] = os.path.join(events_dir, name)
                    fm["url"] = f"{self.baseurl}/events/{name[:-3]}/"
                    self.site_data["events"].append(fm)
                    
        components_dir = os.path.join(WORKSPACE, "_components")
        if os.path.exists(components_dir):
            for root, dirs, files in os.walk(components_dir):
                for name in files:
                    if name.endswith(".md") or name.endswith(".html"):
                        path = os.path.join(root, name)
                        fm, body = read_file_with_front_matter(path)
                        fm["content"] = render_markdown(body)
                        fm["source_body"] = body
                        fm["source_path"] = path
                        
                        if "assembly_guide" in fm:
                            fm["assembly_guide_html"] = render_markdown(fm["assembly_guide"])
                        if "testing_guide" in fm:
                            fm["testing_guide_html"] = render_markdown(fm["testing_guide"])
                            
                        fm["slug"] = slugify(fm.get("title", name[:-3]))
                        fm["url"] = f"{self.baseurl}/components/{fm['slug']}/"
                        self.site_data["components"].append(fm)

    def render_includes(self, text, page_fm):
        def include_replacer(match):
            inc_name = match.group(1).replace(".html", "").strip()
            inc_content = self.includes.get(inc_name, "")
            return self.render_template(inc_content, page_fm)
            
        text = re.sub(r'{%\s*include\s+([a-zA-Z0-9_\-\.]+)\s*%}', include_replacer, text)
        return text

    def render_variables(self, text, page_fm):
        def var_replacer(match):
            var_name = match.group(1).strip()
            
            if var_name == "content":
                return page_fm.get("content", "")
            if var_name == "site.baseurl":
                return self.baseurl
            if var_name == "site.title":
                return self.site_data["title"]
            if var_name == "site.description":
                return self.site_data["description"]
            
            if var_name.startswith("page."):
                key = var_name[5:]
                val = page_fm.get(key, "")
                if isinstance(val, list):
                    return ""
                return str(val)
            
            return match.group(0)
            
        text = re.sub(r'{{\s*([a-zA-Z0-9_\-\.]+)\s*}}', var_replacer, text)
        return text

    def render_loops_and_conditionals(self, text, page_fm):
        if "{% for person in site.data.people %}" in text:
            people_html = ""
            for p in self.site_data["data"]["people"] or []:
                people_html += f"""
                <div class="contributor-profile-card">
                  <h3 class="contributor-name">{p.get('name', '')}</h3>
                  <span class="contributor-role">{p.get('role', '')}</span>
                  <span class="contributor-affiliation">{p.get('affiliation', '')}</span>
                  <p class="contributor-bio">{p.get('bio', '')}</p>
                </div>
                """
            text = re.sub(r'{%\s*for\s+person\s+in\s+site\.data\.people\s*%}.*?{%\s*endfor\s*%}', people_html, text, flags=re.DOTALL)

        if "{% for inst in site.data.institutions %}" in text:
            inst_html = ""
            for inst in self.site_data["data"]["institutions"] or []:
                inst_html += f"""
                <div class="partner-logo-card">
                  <h4 class="partner-name-h4">{inst.get('name', '')}</h4>
                  <span style="font-size: 0.75rem; font-weight:700; color: var(--color-text-light); text-transform:uppercase;">{inst.get('fullname', '')}</span>
                  <p class="partner-desc">{inst.get('description', '')}</p>
                  <a href="{inst.get('link', '#')}" target="_blank" class="partner-link-btn">Visit Website <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                </div>
                """
            text = re.sub(r'{%\s*for\s+inst\s+in\s+site\.data\.institutions\s*%}.*?{%\s*endfor\s*%}', inst_html, text, flags=re.DOTALL)

        if '{% assign sorted_events = site.events | sort: "date" | reverse %}' in text or "site.events" in text:
            events_html = ""
            sorted_evs = sorted(self.site_data["events"], key=lambda x: x.get("date", ""), reverse=True)
            for ev in sorted_evs:
                sites_tags = "".join([f'<span class="site-badge-tag">{s}</span>' for s in ev.get("participating_sites", [])])
                
                mats_links = ""
                for mat in ev.get("materials", []):
                    m_path = mat.get('path', '')
                    m_name = mat.get('name', '')
                    icon = '<i class="fa-solid fa-circle-play text-primary"></i>' if '.mp4' in m_path else ('<i class="fa-solid fa-file-pdf text-red"></i>' if '.pdf' in m_path else '<i class="fa-solid fa-file-lines text-secondary"></i>')
                    target = 'target="_blank"' if ('.pdf' in m_path or '.mp4' in m_path) else ""
                    mats_links += f'<a href="{self.baseurl}{m_path}" class="material-link-btn" {target}>{icon} {m_name}</a>\n'
                
                gallery_imgs = ""
                for img in ev.get("images", []):
                    g_path = img.get('path', '')
                    g_alt = img.get('alt', ev.get('title', ''))
                    g_cap = img.get('caption', '')
                    gallery_imgs += f"""
                    <div class="gallery-photo-frame">
                      <img src="{self.baseurl}{g_path}" alt="{g_alt}" class="gallery-img">
                      {f'<span class="gallery-img-caption">{g_cap}</span>' if g_cap else ''}
                    </div>
                    """
                
                date_str = ev.get('date', '')
                if hasattr(date_str, 'strftime'):
                    date_str = date_str.strftime('%B %Y')
                
                events_html += f"""
                <div class="timeline-event-card">
                  <div class="timeline-marker">
                    <div class="marker-dot"></div>
                    <div class="marker-line"></div>
                  </div>
                  <div class="event-card-content">
                    <div class="event-header-info">
                      <span class="event-date-tag"><i class="fa-regular fa-calendar-days"></i> {date_str}</span>
                      <span class="event-location-tag"><i class="fa-solid fa-location-dot"></i> {ev.get('location', '')}</span>
                      <h2 class="event-card-title">{ev.get('title', '')}</h2>
                    </div>
                    <div class="event-body-text">{ev.get('content', '')}</div>
                    {f'<div class="event-meta-section"><h4 class="meta-section-title"><i class="fa-solid fa-map-location-dot"></i> Participating Sites</h4><div class="tags-row">{sites_tags}</div></div>' if sites_tags else ''}
                    {f'<div class="event-meta-section"><h4 class="meta-section-title"><i class="fa-solid fa-book-open"></i> Training Materials & Resources</h4><div class="materials-links-row">{mats_links}</div></div>' if mats_links else ''}
                    {f'<div class="event-meta-section"><h4 class="meta-section-title"><i class="fa-solid fa-images"></i> Session Gallery</h4><div class="event-photo-gallery">{gallery_imgs}</div></div>' if gallery_imgs else ''}
                  </div>
                </div>
                """
            text = re.sub(r'{%\s*for\s+ev\s+in\s+sorted_events\s*%}.*?{%\s*endfor\s*%}', events_html, text, flags=re.DOTALL)

        return text

    def render_scanner_dashboard(self, text, page_fm):
        scanner_id = page_fm.get("scanner_id")
        if not scanner_id:
            return text
            
        comps = [c for c in self.site_data["components"] if c.get("scanner_id") == scanner_id]
        
        sidebar_buttons = ""
        for c in comps:
            sidebar_buttons += f"""
            <button class="sidebar-node-btn" data-component-id="{c['slug']}" data-subsystem="{c.get('category', '')}">
              {c.get('title', '')}
            </button>
            """
        text = text.replace('{% for comp in scanner_components %}\n            <button class="sidebar-node-btn" data-component-id="{{ comp.title | slugify }}" data-subsystem="{{ comp.category }}">\n              {{ comp.title }}\n            </button>\n          {% endfor %}', sidebar_buttons)
        
        detail_views = ""
        for c in comps:
            slug = c["slug"]
            subsystem_tag = c.get("category", "").upper()
            
            bom_html = ""
            if "bom" in c and c["bom"]:
                bom_rows = ""
                for part in c["bom"]:
                    p_name = part.get("item", "")
                    p_qty = part.get("qty", 1)
                    p_price = part.get("price", "Included")
                    p_link = part.get("link")
                    
                    link_btn = ""
                    if p_link:
                        brand_icon = '<i class="fa-brands fa-amazon"></i> Amazon' if 'amazon' in p_link else ('<i class="fa-solid fa-microchip"></i> DigiKey' if 'digikey' in p_link else '<i class="fa-solid fa-cart-shopping"></i> Purchase')
                        link_btn = f'<a href="{p_link}" target="_blank" class="buy-btn">{brand_icon}</a>'
                    else:
                        link_btn = '<span class="no-link-badge">Local/Custom</span>'
                        
                    bom_rows += f"""
                    <tr>
                      <td class="part-name"><strong>{p_name}</strong></td>
                      <td class="part-qty">{p_qty}</td>
                      <td class="part-price">{p_price}</td>
                      <td class="part-link">{link_btn}</td>
                    </tr>
                    """
                bom_html = f"""
                <div class="tab-sheet-content" data-section="bom">
                  <div class="sheet-article">
                    <h3 class="sheet-sub-title">Bill of Materials</h3>
                    <p class="sheet-desc">List of off-the-shelf and custom parts required to reproduce this component:</p>
                    <div class="bom-table-wrapper">
                      <div class="bom-search-box">
                        <i class="fa-solid fa-magnifying-glass search-icon"></i>
                        <input type="text" class="bom-filter-input" placeholder="Search parts by name, vendor, or specifications..." onkeyup="filterBomTable(this)">
                      </div>
                      <table class="bom-table">
                        <thead>
                          <tr>
                            <th>Part Name / Description</th>
                            <th>Qty</th>
                            <th>Price (Est.)</th>
                            <th>Source / Purchase Link</th>
                          </tr>
                        </thead>
                        <tbody>
                          {bom_rows}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
                """
            
            downloads_html = ""
            if "downloads" in c and c["downloads"]:
                dl_cards = ""
                for file in c["downloads"]:
                    f_name = file.get("name", "")
                    f_path = file.get("path", "")
                    f_ext = f_path.split('.')[-1].upper()
                    icon_class = "fa-solid fa-cube text-primary" if ".stl" in f_path.lower() else "fa-solid fa-drafting-compass text-secondary"
                    dl_cards += f"""
                    <a href="{self.baseurl}{f_path}" download class="download-card">
                      <div class="download-card-icon">
                        <i class="{icon_class}"></i>
                      </div>
                      <div class="download-card-info">
                        <span class="file-title">{f_name}</span>
                        <span class="file-ext">{f_ext} File</span>
                      </div>
                      <span class="download-arrow"><i class="fa-solid fa-arrow-down-long"></i></span>
                    </a>
                    """
                downloads_html = f"""
                <div class="tab-sheet-content" data-section="downloads">
                  <div class="sheet-article">
                    <h3 class="sheet-sub-title">Design & Manufacturing Files</h3>
                    <p class="sheet-desc">Download custom CAD geometries and manufacturing files directly from the repository:</p>
                    <div class="download-links-grid">
                      {dl_cards}
                    </div>
                  </div>
                </div>
                """
            
            video_html = ""
            if "video_url" in c and c["video_url"]:
                video_html = f"""
                <div class="video-player-container">
                  <video controls class="assembly-video">
                    <source src="{self.baseurl}{c['video_url']}" type="video/mp4">
                    Your browser does not support the video tag.
                  </video>
                  <span class="video-caption"><i class="fa-solid fa-circle-play"></i> Assembly Demonstration Video</span>
                </div>
                """
            
            tab_headers = f'<button class="section-tab-btn active" data-section="overview"><i class="fa-solid fa-info-circle"></i> Overview</button>'
            if bom_html:
                tab_headers += f'<button class="section-tab-btn" data-section="bom"><i class="fa-solid fa-list-check"></i> BOM</button>'
            if downloads_html:
                tab_headers += f'<button class="section-tab-btn" data-section="downloads"><i class="fa-solid fa-download"></i> CAD / STL</button>'
            tab_headers += f"""
            <button class="section-tab-btn" data-section="assembly"><i class="fa-solid fa-screwdriver-wrench"></i> Assembly</button>
            <button class="section-tab-btn" data-section="testing"><i class="fa-solid fa-flask"></i> Testing & QA</button>
            """

            detail_views += f"""
            <div class="component-detail-view" id="details-{slug}" data-subsystem="{c.get('category', '')}">
              <div class="detail-header-card">
                <span class="detail-category-tag">{subsystem_tag}</span>
                <h2 class="detail-title">{c.get('title', '')}</h2>
                <p class="detail-short-desc">{c.get('description', '')}</p>
              </div>
              
              <div class="detail-sections-tabs">
                {tab_headers}
              </div>
              
              <div class="detail-tab-sheets">
                <div class="tab-sheet-content active" data-section="overview">
                  <div class="sheet-article">{c.get('content', '')}</div>
                </div>
                {bom_html}
                {downloads_html}
                <div class="tab-sheet-content" data-section="assembly">
                  <div class="sheet-article">
                    <h3 class="sheet-sub-title">Assembly Instructions</h3>
                    {video_html}
                    <div class="guide-steps-list">{c.get('assembly_guide_html', '')}</div>
                  </div>
                </div>
                <div class="tab-sheet-content" data-section="testing">
                  <div class="sheet-article">
                    <h3 class="sheet-sub-title">Testing & Verification</h3>
                    <div class="guide-steps-list">{c.get('testing_guide_html', '')}</div>
                  </div>
                </div>
              </div>
            </div>
            """
            
        pattern = r'{%\s*for\s+comp\s+in\s+scanner_components\s*%}.*?{%\s*endfor\s*%}'
        text = re.sub(pattern, detail_views, text, flags=re.DOTALL)
        
        return text

    def render_template(self, template_str, page_fm):
        template_str = self.render_includes(template_str, page_fm)
        template_str = self.render_variables(template_str, page_fm)
        template_str = self.render_loops_and_conditionals(template_str, page_fm)
        template_str = self.render_scanner_dashboard(template_str, page_fm)
        return template_str

    def build_page(self, src_path, dest_dir, filename="index.html"):
        fm, body = read_file_with_front_matter(src_path)
        layout_name = fm.get("layout", "default")
        
        if src_path.endswith(".md"):
            page_content = render_markdown(body)
        else:
            page_content = body
            
        page_fm = {**fm, "content": page_content}
        
        rendered_content = page_content
        current_layout = layout_name
        
        while current_layout and current_layout in self.layouts:
            layout_template = self.layouts[current_layout]
            rendered_content = self.render_template(layout_template, {**page_fm, "content": rendered_content})
            if current_layout in ["page", "scanner", "events", "component"]:
                current_layout = "default"
            else:
                current_layout = None
                
        rendered_content = self.render_template(rendered_content, page_fm)
        
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, filename)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(rendered_content)
        print(f"Compiled page: {dest_path}")

    def build_site(self):
        print("Starting local build compiler...")
        if os.path.exists(SITE_DIR):
            for root, dirs, files in os.walk(SITE_DIR):
                for f in files:
                    try:
                        os.chmod(os.path.join(root, f), stat.S_IWRITE)
                        os.remove(os.path.join(root, f))
                    except Exception as e:
                        pass
        else:
            os.makedirs(SITE_DIR, exist_ok=True)
        
        self.load_layouts_and_includes()
        self.load_collections()
        
        assets_src = os.path.join(WORKSPACE, "assets")
        if os.path.exists(assets_src):
            shutil.copytree(assets_src, os.path.join(SITE_DIR, "assets"), dirs_exist_ok=True)
            
        images_src = os.path.join(WORKSPACE, "images")
        if os.path.exists(images_src):
            shutil.copytree(images_src, os.path.join(SITE_DIR, "images"), dirs_exist_ok=True)

        ernie_src = os.path.join(WORKSPACE, "ERNIE")
        if os.path.exists(ernie_src):
            shutil.copytree(ernie_src, os.path.join(SITE_DIR, "ERNIE"), dirs_exist_ok=True)
            
        hardware_src = os.path.join(WORKSPACE, "Hardware")
        if os.path.exists(hardware_src):
            shutil.copytree(hardware_src, os.path.join(SITE_DIR, "Hardware"), dirs_exist_ok=True)
            
        # Build Root Pages
        self.build_page(os.path.join(WORKSPACE, "index.html"), SITE_DIR, "index.html")
        self.build_page(os.path.join(WORKSPACE, "about.html"), os.path.join(SITE_DIR, "about"), "index.html")
        self.build_page(os.path.join(WORKSPACE, "events.html"), os.path.join(SITE_DIR, "events"), "index.html")
        self.build_page(os.path.join(WORKSPACE, "scanners", "index.html"), os.path.join(SITE_DIR, "scanners"), "index.html")
        self.build_page(os.path.join(WORKSPACE, "scanners", "ernie.html"), os.path.join(SITE_DIR, "scanners", "ernie"), "index.html")
        self.build_page(os.path.join(WORKSPACE, "scanners", "imagine.html"), os.path.join(SITE_DIR, "scanners", "imagine"), "index.html")
        
        # Build Component standalone pages directly using the collection entries loaded
        for comp in self.site_data["components"]:
            slug = comp["slug"]
            self.build_page(comp["source_path"], os.path.join(SITE_DIR, "components", slug), "index.html")

        print("Build Completed successfully!")

if __name__ == "__main__":
    builder = PreviewBuilder()
    builder.build_site()
