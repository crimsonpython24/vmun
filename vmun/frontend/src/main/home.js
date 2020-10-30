import React, { useContext } from 'react';
import "antd/dist/antd.css";

import { Redirect } from "react-router-dom";
import { VmunContext } from '../vmun/context';

function Home() {
  const [state, dispatch] = useContext(VmunContext);
  if (state.user.id == -1) {
    return <Redirect to={'/welcome'} />
  }
  return <h1>Home</h1>
}

export default Home;