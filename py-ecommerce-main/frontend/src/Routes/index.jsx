import { useRoutes } from 'react-router-dom';
import Home from '../Pages/Home';
import Products from '../Pages/Products';

function Routes() {
  const appRoutes = useRoutes([
    { path: '/', element: <Home /> },
    { path: '/products', element: <Products /> },
  ]);

  return appRoutes;
}

export default Routes;
