import React from "react";
import { Routes, Route } from "react-router-dom";
import Content from "./Content";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Content />} />
      </Routes>
    </div>
  );
};

export default App;
