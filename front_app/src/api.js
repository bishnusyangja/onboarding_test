import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000';

const getRequest = () => {
    axios.defaults.baseURL = BASE_URL;
    axios.defaults.headers.common['Content-Type'] = 'application/json';
    return axios
}

export default Request = {

    get : (url, params) => {
        return getRequest().get(url, {params: params});
    },

    post : (url, data) => {
        return getRequest().post(url, data)
    },

    patch : (url, data, params) => {
        return getRequest().patch(url, data, {params: params});
    },

    del : (url, params) => {
        return getRequest().delete(url, {params: params});
    },
}
