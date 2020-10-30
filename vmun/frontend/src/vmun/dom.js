import React, { useContext } from 'react';

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "../../src/main/home";
import Feedback from "../../src/main/feedback";
import Development from "../../src/main/development";
import Articles from "../../src/main/articles";
import Welcome from "../../src/main/welcome";
import Login from "../../src/auth/login-dom";
import Signup from "../../src/auth/signup-dom";

import Navbar from "../../src/common/navbar";

import { VmunContext } from './context';


const Vmun = () => {
  const [state, dispatch] = useContext(VmunContext);
  return (
    <>
      <Router>
        <Navbar/>
        <Switch>
          <Route exact path="/">
            <Home/>
            <h2>Account: {state.user.id || -1} | {state.user.username}</h2>
          </Route>
          <Route path="/accounts/login"><Login/></Route>
          <Route path="/accounts/signup"><Signup/></Route>
          <Route path="/feedback"><Feedback/></Route>
          <Route path="/development"><Development/></Route>
          <Route path="/articles"><Articles/></Route>
          <Route path="/welcome"><Welcome/></Route>
        </Switch>
      </Router>

    </>
  );
};

export default Vmun;
