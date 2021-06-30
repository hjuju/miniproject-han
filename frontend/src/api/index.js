import axios from "axios";

// 이곳은 리액트가 아닌 axios
// 프로토콜은 header와 body로 이루어져 있다.
const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type': 'application/json'} //image/jpeg로 바꾸면 이미지 업로드
const headers_xml = {'Content-Type': 'application/xml'} //xml로 처리할때

export const userSignup = body => axios.post(`${SERVER}member/signup`, {headers, body}) // post로 주면 보안방식으로 됨
export const userLogin = body => axios.get(`${SERVER}member/login/${body.username}/`, {headers, body}) //body란 이름으로 간략하게 
export const blogpostWrite = body => axios.post(`${SERVER}board/postwrite`, {headers, body})