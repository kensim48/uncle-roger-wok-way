import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "http://localhost:8000/";

class UserService {
  getPublicContent() {
    return axios.get(API_URL + "all");
  }

  getUserDetails() {
    return axios.get(API_URL + "auth/users/me/", { headers: authHeader() });
  }

  getModeratorBoard() {
    return axios.get(API_URL + "mod", { headers: authHeader() });
  }

  getAdminBoard() {
    return axios.get(API_URL + "admin", { headers: authHeader() });
  }
}

export default new UserService();
