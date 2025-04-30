import { useContext } from 'react';
import { AppContext } from '../../Context';
import Layout from '../../Components/Layout';
import Card from '../../Components/Card';

const Home = () => {
  const { products } = useContext(AppContext);

  return (
    <Layout title='Home'>
      <section className='grid grid-cols-4 justify-center gap-8 w-full  px-8'>
        {products?.map((product, index) => (
          <Card key={index} product={product} />
        ))}
      </section>
    </Layout>
  );
};

export default Home;
