import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Services = () => {
  const [services, setServices] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/services')
      .then(response => setServices(response.data))
      .catch(error => console.error("Error fetching services:", error));
  }, []);

  return (
    <div>
      <h2>Our Services</h2>
      <ul>
        {services.map(service => (
          <li key={service.id}>
            <h3>{service.name}</h3>
            <p>{service.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Services;
