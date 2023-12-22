import spawn from "redux-saga";
import testSaga from "./test-saga";

// Export the root saga
export default function* rootSaga() {
  yield spawn(testSaga);
}
