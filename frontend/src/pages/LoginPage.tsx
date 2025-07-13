import React, { useState } from 'react';
import axios from 'axios';
import { Card, Input, Button } from 'antd';


interface Props {
  onLogin: () => void;
}

const LoginPage: React.FC<Props> = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const API_URL = import.meta.env.VITE_API_URL;

  const handleSubmit = async () => {
    try {
     
      const response = await axios.post(`${API_URL}/auth/login`, {
        username,
        password,
      });
      localStorage.setItem('token', response.data.access_token);
      onLogin();
    } catch {
      setError('Login failed');
    }
  };

  return (
    <Card

      style={{
        maxWidth: 400,
        margin: 'auto',
        marginTop: 100,
        background: '#e0f2ff', // заменили градиент на однотонный голубой
        border: 'none',
        boxShadow: '0 4px 24px rgba(0,0,0,0.08)',
      }}
      styles={{ header: { background: 'transparent', border: 'none' } }}
    >  <div style={{ textAlign: 'center' }}>
          <img
            src="/logo.png"
            alt="Logo"
            style={{ height: 60 }}
          />
        </div>
      <Input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <Input.Password
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ marginTop: 10 }}
        onKeyDown={e => {
          if (e.key === 'Enter') {
            handleSubmit();
          }
        }}
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <Button
          type="primary"
          onClick={handleSubmit}
          style={{ marginTop: 10 }}
        >
          Войти
        </Button>
      </div>
    </Card>
  );
};

export default LoginPage;