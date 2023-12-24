import "./App.css";
import { Headers } from "./components/Headers";
import { TodoList } from "./components/TodoList";

function App() {
  return (
    <>
      <div style={{ margin: "auto", width: "40%" }}>
        <Headers />
        <TodoList />
      </div>
    </>
  );
}

export default App;
