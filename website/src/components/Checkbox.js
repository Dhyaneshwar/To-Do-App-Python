import React from "react";

const Checkbox = (props) => {
  console.log("inside checkbox");
  return (
    <>
      <input type="checkbox" id={props.id} />
      <label htmlFor={props.id}>{props.value}</label>
      <br/>
    </>
  );
};

export default Checkbox;
