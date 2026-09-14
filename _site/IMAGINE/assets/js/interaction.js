/* ==========================================================================
   IMAGINE Website - Client-Side Interactivity (interaction.js)
   Handling schematic node switching, inner tabs, and BOM filtering.
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function() {
  
  // 1. Initial State Setup
  initializeDashboard();
  if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
    MathJax.typesetPromise();
  }

  // 2. Subsystem Selector Event Listeners (Control / Gradients / RF / Magnet / Robot)
  const subsystemBtns = document.querySelectorAll(".subsystem-tab-btn");
  subsystemBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetSubsystem = btn.getAttribute("data-subsystem");
      
      // Update button active states
      subsystemBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      // Swap active SVG schematics
      const schematics = document.querySelectorAll(".schematic-view");
      schematics.forEach(s => s.classList.remove("active"));
      
      const targetSchematic = document.getElementById(`schematic-${targetSubsystem}`);
      if (targetSchematic) {
        targetSchematic.classList.add("active");
      }

      // Filter the component list in the sidebar and activate the first one
      filterSidebarBySubsystem(targetSubsystem);
    });
  });

  // 3. Interactive SVG Node Click Handlers
  const svgNodes = document.querySelectorAll(".interactive-node");
  svgNodes.forEach(node => {
    node.addEventListener("click", () => {
      const componentId = node.getAttribute("data-component-id");
      if (componentId) {
        activateComponent(componentId);
      }
    });
  });

  // 4. Sidebar Button Click Handlers
  const sidebarBtns = document.querySelectorAll(".sidebar-node-btn");
  sidebarBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const componentId = btn.getAttribute("data-component-id");
      if (componentId) {
        activateComponent(componentId);
      }
    });
  });

  // 5. Component Inner Tab Switching (Overview, BOM, Assembly, Testing)
  const tabBtns = document.querySelectorAll(".section-tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const section = btn.getAttribute("data-section");
      const parentView = btn.closest(".component-detail-view");
      
      if (parentView) {
        const btns = parentView.querySelectorAll(".section-tab-btn");
        btns.forEach(b => b.classList.remove("active"));
        
        const sheets = parentView.querySelectorAll(".tab-sheet-content");
        sheets.forEach(s => s.classList.remove("active"));
        
        btn.classList.add("active");
        const activeSheet = parentView.querySelector(`.tab-sheet-content[data-section="${section}"]`);
        if (activeSheet) {
          activeSheet.classList.add("active");
        }
      }
    });
  });

});

/**
 * Initialize Dashboard state.
 * Selects the first available subsystem and filters components.
 */
function initializeDashboard() {
  const activeSubBtn = document.querySelector(".subsystem-tab-btn.active");
  if (activeSubBtn) {
    const activeSub = activeSubBtn.getAttribute("data-subsystem");
    filterSidebarBySubsystem(activeSub);
  }
}

/**
 * Filter sidebar buttons dynamically by the active subsystem.
 */
function filterSidebarBySubsystem(targetSubsystem) {
  const sidebarBtns = document.querySelectorAll(".sidebar-node-btn");
  let firstVisibleBtn = null;

  sidebarBtns.forEach(btn => {
    const btnSub = btn.getAttribute("data-subsystem");
    if (btnSub === targetSubsystem) {
      btn.style.display = "block";
      if (!firstVisibleBtn) {
        firstVisibleBtn = btn;
      }
    } else {
      btn.style.display = "none";
    }
  });

  if (firstVisibleBtn) {
    const componentId = firstVisibleBtn.getAttribute("data-component-id");
    activateComponent(componentId);
  }
}

/**
 * Activate a component across the entire dashboard.
 */
function activateComponent(componentId) {
  if (!componentId) return;

  // 1. Update SVG Nodes
  const svgNodes = document.querySelectorAll(".interactive-node");
  svgNodes.forEach(node => {
    if (node.getAttribute("data-component-id") === componentId) {
      node.classList.add("active");
      const rect = node.querySelector(".node-rect");
      if (rect) {
        rect.style.stroke = "var(--color-gold)";
        rect.style.fill = "var(--color-emerald-deep)";
      }
    } else {
      node.classList.remove("active");
      const rect = node.querySelector(".node-rect");
      if (rect) {
        rect.style.stroke = "#134e5a";
        rect.style.fill = "#09252d";
      }
    }
  });

  // 2. Update Sidebar Buttons
  const sidebarBtns = document.querySelectorAll(".sidebar-node-btn");
  sidebarBtns.forEach(btn => {
    if (btn.getAttribute("data-component-id") === componentId) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  // 3. Swap Documentation Detail Panels
  const detailPanels = document.querySelectorAll(".component-detail-view");
  detailPanels.forEach(panel => {
    if (panel.id === `details-${componentId}`) {
      panel.classList.add("active");
      const firstTab = panel.querySelector(".section-tab-btn[data-section='overview']");
      if (firstTab) {
        firstTab.click();
      }
    } else {
      panel.classList.remove("active");
    }
  });
}

/**
 * Interactive BOM search filter function.
 */
function filterBomTable(inputElement) {
  const filterText = inputElement.value.toLowerCase();
  const tableWrapper = inputElement.closest(".bom-table-wrapper");
  
  if (tableWrapper) {
    const rows = tableWrapper.querySelectorAll(".bom-table tbody tr");
    rows.forEach(row => {
      const partNameCell = row.querySelector(".part-name");
      if (partNameCell) {
        const textValue = partNameCell.textContent || partNameCell.innerText;
        if (textValue.toLowerCase().indexOf(filterText) > -1) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      }
    });
  }
}
