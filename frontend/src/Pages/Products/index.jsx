import { useContext } from 'react';
import Layout from '../../Components/Layout';
import { AppContext } from '../../Context';

const Products = () => {
  const { products } = useContext(AppContext);
  console.log(products);

  return <Layout title={'Productos'}></Layout>;
};

export default Products;
