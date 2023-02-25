import React, { FunctionComponent, useState } from "react";
import Home from "../components/Home";
import Sidebar from "../components/Sidebar";

const Content: FunctionComponent = () => {
  return (
    <section className="flex">
      <Sidebar/>
      <Home/>
    </section>
  );
};

export default Content;
