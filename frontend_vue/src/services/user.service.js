import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "http://localhost:8000/";

class UserService {
  getItemList() {
    return axios.get(API_URL + "api/item_listing/");
  }

  getUserDetails() {
    return axios.get(API_URL + "auth/users/me/", { headers: authHeader() });
  }

  postItemModify(data) {
    return axios.post(API_URL + "api/item_modify/", data, {
      headers: authHeader(),
    });
  }

  getAdminBoard() {
    return axios.get(API_URL + "admin", { headers: authHeader() });
  }
}

export default new UserService();
