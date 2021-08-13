import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "http://localhost:8000/";

class UserService {
  getItemList() {
    return axios.get(API_URL + "api/item_listing/");
  }

  getUserDetails() {
    return axios.get(API_URL + "api/whoami/", { headers: authHeader() });
  }

  postItemModify(data) {
    return axios.post(API_URL + "api/item_modify/", data, {
      headers: authHeader(),
      data: data,
    });
  }

  deleteItemModify(data) {
    return axios.delete(API_URL + "api/item_modify/", {
      data: data,
      headers: authHeader(),
    });
  }

  postOrder(data) {
    return axios.post(API_URL + "api/send_order/", data, {
      headers: authHeader(),
      data: data,
    });
  }
}

export default new UserService();
