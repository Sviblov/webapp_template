// frontend/src/App.tsx
import { useState } from 'react';
import { useEffect } from 'react'; 
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';

import axios from 'axios';


function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
    axios
      .get(`${API_URL}/users/verify`, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(() => setIsAuthenticated(true))
      .catch(() => {
        localStorage.removeItem('token');
        setIsAuthenticated(false);
      });
  }
  }, []);

  if (!isAuthenticated) {
    return <LoginPage onLogin={() => setIsAuthenticated(true)} />;
  }

  return <Dashboard />;
}

export default App;

