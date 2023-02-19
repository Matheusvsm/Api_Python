// carrega todos os produtos existentes na tabela
function loadProducts() {
    console.log("loadProducts")
    $.ajax({
        url: "http://127.0.0.1:5000/products",
        type: "GET",
        success: function(data) {
            var productsTable = $("#products-table tbody");
            productsTable.empty();
            for (var i = 0; i < data.length; i++) {
                var product = data[i];
                productsTable.append("<tr data-id='" + product.id + "'>" +
                    "<td>" + product.id + "</td>" +
                    "<td>" + product.name + "</td>" +
                    "<td>" + product.price + "</td>" +
                    "<td><button class='edit-product-button'>Editar</button> " +
                    "<button class='delete-product-button'>Excluir</button></td>" +
                    "</tr>");
            }
        }
    });
}

// adiciona um novo produto ao banco de dados através da API
function addProduct(name, price) {
    $.ajax({
        url: "http://127.0.0.1:5000/products",
        type: "POST",
        data: { "name": name, "price": price },
        success: function() {
            loadProducts();
        }
    });
}

// atualiza um produto existente no banco de dados através da API
function updateProduct(id, name, price) {
    $.ajax({
        url: "http://127.0.0.1:5000/products/" + id,
        method: "PUT",
        contentType: "application/json",
        data: JSON.stringify({
            name: name,
            price: price
        }),
        success: function(result) {
            alert("Produto atualizado com sucesso!");
            location.reload();
        },
        error: function(xhr, resp, text) {
            console.log(xhr, resp, text);
        }
    });
}
