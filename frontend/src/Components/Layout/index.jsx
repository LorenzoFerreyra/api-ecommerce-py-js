import Navbar from '../Navbar';

const Layout = ({ title, children }) => {
  return (
    <>
      <Navbar />
      <main className='container mx-auto mt-6 p-6 rounded-t-lg bg-neutral-50'>
        <h1 className='w-full text-center text-4xl font-bold mb-6'>{title}</h1>
        {children}
      </main>
    </>
  );
};

export default Layout;
