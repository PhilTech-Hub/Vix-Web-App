import React, { useState } from 'react';
import axios from 'axios';

const RequestService = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        service: '',
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:5000/api/request-service', formData)
            .then(response => alert('Request submitted!'))
            .catch(error => console.error('Error submitting request:', error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h1>Request a Service</h1>
            <input
                type="text"
                name="name"
                placeholder="Your Name"
                value={formData.name}
                onChange={handleChange}
                required
            />
            <input
                type="email"
                name="email"
                placeholder="Your Email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="service"
                placeholder="Requested Service"
                value={formData.service}
                onChange={handleChange}
                required
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default RequestService;
