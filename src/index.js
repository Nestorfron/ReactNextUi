import React from 'react';
import ReactDOM from 'react-dom/client';
import '../src/front/styles/index.css';
import reportWebVitals from './reportWebVitals';
import AppContext from "../src/front/store/AppContext";
import Layout from './Layout';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AppContext>
      <Layout />
    </AppContext> 
  </React.StrictMode>
);

reportWebVitals();
