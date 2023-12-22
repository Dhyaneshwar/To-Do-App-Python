import { createAction } from "@reduxjs/toolkit";

// Declaring types
export const checkRedux = "CHECKING_REDUX";

// Declaring Actions
export const checkReduxAction = createAction(checkRedux);
