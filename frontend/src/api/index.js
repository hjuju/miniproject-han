import { SingleBedTwoTone } from "@material-ui/icons";
import axios from "axios";
import { Login } from "user";

const SERVER = 'http://127.0.0.1:8000/'

export const userSignup = signupRequest => axios.get(`${SERVER}member/signup`, signupRequest)
export const userLogin = loginRequest => axios.get(`${SERVER}member/login`, loginRequest)