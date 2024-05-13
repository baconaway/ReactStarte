import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './Styles.css';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import ImageBanner from './components/ImageBanner';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <ImageBanner imageUrl="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
