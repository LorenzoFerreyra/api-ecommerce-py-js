import { BrowserRouter as Router } from 'react-router-dom';
import { AppContextProvider as Provider } from '../Context';
import Routes from '../Routes';

function App() {
  return (
    <Provider>
      <Router>
        <Routes />
      </Router>
    </Provider>
  );
}

export default App;
