const Card = ({ product }) => {
  const isAvailable = product.stock > 0;
  return (
    <article className='flex flex-col'>
      <img
        src={product.img}
        alt={product.name}
        className='w-full h-48 bg-slate-200 rounded-lg  object-cover'
      />
      <div className='grow flex flex-wrap justify-between mt-2 px-4'>
        <h4 className='font-semibold text-lg w-full'>{product.name}</h4>
        <p className='text-neutral-500 self-center'>
          {product.size || (isAvailable ? 'En stock' : 'Agotado')}
        </p>
        <p className='font-semibold text-xl'>${product.price}</p>
      </div>
      <div className='flex gap-4 justify-center mt-2'>
        <button className='px-8 py-2 bg-slate-300 rounded-full hover:bg-slate-400/60 hover:cursor-pointer transition'>
          Agregar
        </button>
        <button className='px-8 py-2 bg-slate-900 rounded-full text-neutral-50 hover:bg-slate-800 hover:cursor-pointer transition'>
          Comprar
        </button>
      </div>
      <p></p>
    </article>
  );
};

export default Card;
