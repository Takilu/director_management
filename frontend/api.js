
const API_URL = 'http://localhost:8000/api/';
const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Token ${localStorage.getItem('token')}`
};


export const login = async (email, password) => {
    const response = await fetch(`${API_URL}auth/login/`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email, password})
    });
    const data = await response.json();
    localStorage.setItem('token', data.token);
    return data.user; // Returns user object with role info
  };

  export const logout = () => {
    localStorage.removeItem('token');
  };


  export const getTrainers = async (searchQuery = '') => {
    const response = await fetch(`${API_URL}trainers/?search=${searchQuery}`, {
      headers
    });
    return response.json();
  };


  export const updateTrainer = async (id, data) => {
    const response = await fetch(`${API_URL}trainers/${id}/`, {
      method: 'PUT',
      headers,
      body: JSON.stringify(data)
    });
    return response.json();
  };


  export const createTraining = async (trainingData) => {
    const response = await fetch(`${API_URL}training-types/`, {
      method: 'POST',
      headers,
      body: JSON.stringify(trainingData)
    });
    return response.json();
  };


  export const signContract = async (contractData) => {
    const response = await fetch(`${API_URL}contracts/`, {
      method: 'POST',
      headers,
      body: JSON.stringify(contractData)
    });
    return response.json();
  };