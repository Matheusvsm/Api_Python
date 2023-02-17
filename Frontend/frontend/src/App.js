import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <Router>
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <Link to={"/"} className="navbar-brand">
            CRUD de Produtos
          </Link>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item">
                <Link to={"/"} className="nav-link">
                  Listar Produtos
                </Link>
              </li>
              <li className="nav-item">
                <Link to={"/create"} className="nav-link">
                  Criar Produto
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        <Switch>
          <Route exact path="/" component={ProductList} />
          <Route exact path="/create" component={CreateProduct} />
          <Route exact path="/edit/:id" component={EditProduct} />
        </Switch>
      </div>
    </Router>
  );
}
function EditProduct() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const { id } = useParams();

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/products/${id}`).then((response) => {
      setName(response.data.name);
      setPrice(response.data.price);
    });
  }, [id]);

  function onSubmit(event) {
    event.preventDefault();

    const product = {
      name: name,
      price: price,
    };

    axios.put(`http://127.0.0.1:5000/products/${id}`, product).then((response) => {
      console.log(response.data);
    });
  }

  return (
    <div>
      <h3>Editar Produto</h3>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label>Nome do Produto: </label>
          <input
            type="text"
            className="form-control"
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Preço do Produto: </label>
          <input
            type="text"
            className="form-control"
            value={price}
            onChange={(event) => setPrice(event.target.value)}
          />
        </div>
        <div className="form-group">
          <input type="submit" value="Editar Produto" className="btn btn-primary" />
        </div>
      </form>
    </div>
  );
}

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/products").then((response) => {
      setProducts(response.data);
    });
  }, []);

  function deleteProduct(id) {
    axios.delete(`http://127.0.0.1:5000/products/${id}`).then((response) => {
      setProducts(products.filter((p) => p._id !== id));
    });
  }

  return (
    <div className="mt-3">
      <h3>Listar Produtos</h3>
      <table className="table table-striped mt-3">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Preço</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product._id}>
              <td>{product._id}</td>
              <td>{product.name}</td>
              <td>{product.price}</td>
              <td>
                <Link to={"/edit/" + product._id} className="btn btn-sm btn-primary mr-1">
                  Editar
                </Link>
                <button className="btn btn-sm btn-danger" onClick={() => deleteProduct(product._id)}>
                  Apagar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function CreateProduct() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  function onSubmit(event) {
    event.preventDefault();

    const product = {
      name: name,
      price: price,
    };

    axios.post("http://127.0.0.1:5000/products", product).then((response) => {
      console.log(response.data);
    });

    setName("");
    setPrice("");
  }

  return (
    <div className="mt-3">
      <h3>Criar Produto</h3>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label>Nome: </label>
          <input type="text" className="form-control" value={name} onChange={(e) => setName(e.target.value)} />
        </div>
        <div className="form-group">
          <label>Preço: </label>
          <input type="text" className="form-control" value={price} onChange={(e) => setPrice(e.target.value)} />
        </div>
        <div className="form-group">
          <input type="submit" value="Criar Produto" className="btn btn-primary" />
        </div>
      </form>
    </div>
  );
}
