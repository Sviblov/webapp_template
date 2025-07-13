import React, {useEffect, useState} from 'react';
import axios from 'axios';
import { Spin, Typography, Space, Row, Col, Card, Divider } from 'antd';


const { Title } = Typography;
const API_URL = import.meta.env.VITE_API_URL;

const Dashboard: React.FC = () => {

  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  const token = localStorage.getItem('token');

  axios.get(`${API_URL}/users/getuser`, {
    headers: {
      Authorization: `Bearer ${token}`,
    }
  })
    .then(res => {
      setUser(res.data);
      setLoading(false);
    })
    .catch(err => {
      console.error('Ошибка при загрузке пользователя', err);
      setLoading(false);
    });
}, []);

  

  return (
   <Row justify="center" align="middle" style={{ minHeight: '100vh', background: '#fff' }}>
  <Col xs={24} sm={22} md={20} lg={18} xl={16}>
        <Card style={{ borderRadius: 12, boxShadow: '0 4px 24px rgba(0,0,0,0.08)', background: '#e0f2ff', padding: 0 }}>
          <Title level={2} style={{ textAlign: 'center', marginBottom: 24 }}>User Info</Title>
          <Divider />
          <Space direction="vertical" size="large" style={{ width: '100%' }}>
          </Space>
           {loading ? (
              <Spin />
            ) : user ? (
              <Card type="inner" title={user.username} style={{ background: '#ffffff' }}>
                <p>Email: {user.email}</p>
                <p>ID: {user.id}</p>
              </Card>
            ) : (
              <p>Нет данных</p>
            )}
        </Card>
      </Col>
    </Row>
  );
};

export default Dashboard;