import axios from "axios";

const API_URL = "http://localhost:8000/auth/jwt/";

class AuthService {
  login(user) {
    return axios
      .post(API_URL + "create/", {
        username: user.username,
        password: user.password,
      })
      .then((response) => {
        if (response.data.access) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    console.log("run");
    localStorage.removeItem("user");
  }

  register(user) {
    return axios.post(API_URL + "signup", {
      username: user.username,
      email: user.email,
      password: user.password,
    });
  }
}

export default new AuthService();
