import { NavLink } from 'react-router-dom';
import { TiShoppingCart } from 'react-icons/ti';

const Navbar = () => {
  const navLinkStyle = isActive => {
    const relativeStyle = isActive ? 'bg-slate-50 font-medium' : '';
    return ` rounded-lg px-4 py-3 ${relativeStyle} hover:bg-slate-100 transition`;
  };

  return (
    <header className='w-full h-60 px-12 bg-center bg-[url(https://plus.unsplash.com/premium_photo-1681488262364-8aeb1b6aac56?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)]'>
      <nav className='w-full h-20 grid grid-cols-3 place-items-center px-6 rounded-b-lg bg-neutral-50/80'>
        <div className='justify-self-start'>
          <h3 className='text-2xl font-bold'>
            <NavLink to='/'>Py-Ecommerce</NavLink>
          </h3>
        </div>
        <ul className='w-fit flex justify-center gap-4 grow'>
          <li>
            <NavLink
              to='/'
              className={({ isActive }) => navLinkStyle(isActive)}
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              to='/products'
              className={({ isActive }) => navLinkStyle(isActive)}
            >
              Productos
            </NavLink>
          </li>
          <li>
            <NavLink
              to='/orders'
              className={({ isActive }) => navLinkStyle(isActive)}
            >
              Pedidos
            </NavLink>
          </li>
        </ul>
        <ul className='justify-self-end flex gap-4'>
          <li>
            <NavLink
              to='/login'
              className={({ isActive }) => navLinkStyle(isActive)}
            >
              Login
            </NavLink>
          </li>
          <li>
            <NavLink to='/cart'>
              <TiShoppingCart className='h-6 w-6' />
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
