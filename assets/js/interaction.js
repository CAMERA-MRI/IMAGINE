/* ==========================================================================
   IMAGINE Website - Client-Side Interactivity (interaction.js)
   Handling schematic node switching, inner tabs, and BOM filtering.
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function() {
  
  // 1. Initial State Setup
  initializeDashboard();

  // 2. Subsystem Selector Event Listeners (Control / Gradients / RF / etc.)
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

      // Automatically select the first component of this subsystem in the list
      selectFirstComponentInSubsystem(targetSubsystem);
    });
  });

  // 3. Interactive SVG Node Click Handlers
  const svgNodes = document.querySelectorAll(".interactive-node");
  svgNodes.forEach(node => {
    node.addEventListener("click", () => {
      const componentId = node.getAttribute("data-component-id");
      activateComponent(componentId);
    });
  });

  // 4. Sidebar Button Click Handlers
  const sidebarBtns = document.querySelectorAll(".sidebar-node-btn");
  sidebarBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const componentId = btn.getAttribute("data-component-id");
      activateComponent(componentId);
    });
  });

  // 5. Component Inner Tab Switching (Overview, BOM, Assembly, Testing)
  const tabBtns = document.querySelectorAll(".section-tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const section = btn.getAttribute("data-section");
      const parentView = btn.closest(".component-detail-view");
      
      if (parentView) {
        // Deactivate all tab buttons and sheet content within this specific view
        const btns = parentView.querySelectorAll(".section-tab-btn");
        btns.forEach(b => b.classList.remove("active"));
        
        const sheets = parentView.querySelectorAll(".tab-sheet-content");
        sheets.forEach(s => s.classList.remove("active"));
        
        // Activate current tab button and sheet
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
 * Selects the first available component to display on load.
 */
function initializeDashboard() {
  const activeSubBtn = document.querySelector(".subsystem-tab-btn.active");
  if (activeSubBtn) {
    const activeSub = activeSubBtn.getAttribute("data-subsystem");
    selectFirstComponentInSubsystem(activeSub);
  }
}

/**
 * Find the first component in a given subsystem and activate it.
 */
function selectFirstComponentInSubsystem(subsystemId) {
  // Find first sidebar button matching this subsystem
  const firstBtn = document.querySelector(`.sidebar-node-btn[data-subsystem="${subsystemId}"]`);
  if (firstBtn) {
    const componentId = firstBtn.getAttribute("data-component-id");
    activateComponent(componentId);
  }
}

/**
 * Activate a component across the entire dashboard:
 * - Highlights the SVG node (matching data-component-id)
 * - Highlights the Sidebar button (matching data-component-id)
 * - Shows the documentation detail panel (matching id = details-{component-id})
 */
function activateComponent(componentId) {
  // 1. Update SVG Nodes
  const svgNodes = document.querySelectorAll(".interactive-node");
  svgNodes.forEach(node => {
    if (node.getAttribute("data-component-id") === componentId) {
      node.classList.add("active");
      // If there's an internal rect shape inside the node group, style it
      const rect = node.querySelector(".node-rect");
      if (rect) {
        rect.style.stroke = "var(--color-gold)";
        rect.style.fill = "var(--color-emerald-deep)";
      }
    } else {
      node.classList.remove("active");
      const rect = node.querySelector(".node-rect");
      if (rect) {
        rect.style.stroke = "#255842";
        rect.style.fill = "#153326";
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
      
      // Auto-reset tabs within the newly activated panel to 'Overview'
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
 * Triggered onkeyup in the BOM search box.
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
