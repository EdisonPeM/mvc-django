const setupDataTable = (tableId) => {
  new simpleDatatables.DataTable(tableId, {
    labels: {
      placeholder: "Buscar...",
      searchTitle: "Buscar en la tabla",
      perPage: "Entradas por página",
      pageTitle: "Página {page}",
      info: "Mostrando {start} a {end} de {rows} entradas",
      noResults: "No se encontraron resultados para esta busqueda",
    },
    scrollY: '50dvh',
    // perPage: 5,
    perPageSelect: false,
    searchQuerySeparator: ',',
    classes: {
      // Table Containers
      top: "mb-2 d-flex justify-content-between",
      headercontainer: "custom-table-headercontainer",
      container: "custom-table-container",
      empty: "custom-table-empty",
      bottom: "mt-2 d-flex flex-wrap justify-content-center justify-content-md-between gap-2",

      // Pagination
      pagination: "pagination-container",
      paginationList: "pagination mb-0",
      paginationListItem: "page-item",
      paginationListItemLink: "page-link",
      hidden: 'invisible',
      active: "active",
      disabled: 'disabled',

      // Per Page Selector
      selector: "form-select d-inline-block w-auto me-2",

      // Search Input
      input: "form-control",

      // Sorter
      sorter: "custom-table-sorter"
    }
  })
};