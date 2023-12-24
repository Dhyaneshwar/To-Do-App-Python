import React, { useState } from "react";
import Checkbox from "./Checkbox";
import { AddTodo } from "./AddTodo";

export const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [todoCompleted, setTodoCompleted] = useState(-1);

  if (todoCompleted !== -1) {
    const newTodos = todos.filter((_, index) => index !== todoCompleted);
    setTodos(newTodos);
    setTodoCompleted(-1);
  }

  return (
    <>
      {todos.map((todo, index) => (
        <Checkbox
          key={`${index}_${todo}`}
          id={index}
          value={todo}
          setTodoCompleted={setTodoCompleted}
        />
      ))}
      {todos.length === 0 && <h5>Please Add a New Todo</h5>}
      <AddTodo setTodos={setTodos} />
    </>
  );
};
