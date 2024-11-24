import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Headers/Header';
import Footer from './components/Footers/Footer';
import Home from './pages/Home';
import Services from './pages/Services/Service';
import Login from './pages/Login';

const App = () => (
  <Router>
    <Header />
    <main>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </main>
    <Footer />
  </Router>
);

export default App;
