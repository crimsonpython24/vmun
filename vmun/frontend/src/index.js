import React from "react";
import ReactDOM from "react-dom";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import DevIndex from "./dev/index";


function Todo() {
  return <h2>Todo</h2>;
}

function Home() {
  return <h2>Home</h2>;
}

export default function main() {
  return (
    <>
      <h1>Test Project</h1>
      <Router>
        <div>
          <nav>
            <ul>
              <li><Link to="/">Home</Link>
              </li>
              <li><Link to="/todos">Developing area</Link></li>
            </ul>
          </nav>
        </div>
        <Switch>
          <Route path="/todos" component={DevIndex}/>
          <Route path="/" component={Home}/>
        </Switch>
      </Router>
    </>
  )
}

ReactDOM.render(main(), document.getElementById("root"));