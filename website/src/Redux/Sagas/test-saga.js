import takeEvery from "redux-saga";
import { checkRedux } from "../Actions/test-action";

function* handleCheckRedux() {
  console.log("handler is called");
  yield 1; // this line is not required.
}

export default function* todoSaga() {
  yield takeEvery(checkRedux, handleCheckRedux);
}
