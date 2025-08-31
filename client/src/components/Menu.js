import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ShoppingCart } from 'lucide-react';
import { useCart } from '../context/CartContext';
import toast from 'react-hot-toast';

const Menu = () => {
  const [activeCategory, setActiveCategory] = useState('starters');
  const { addToCart } = useCart();

  const menuData = {
    starters: [
      {
        id: 'samosa',
        name: 'Samosas',
        description: 'Crispy pastry filled with spiced potatoes and peas',
        price: 8.99,
        image: '🍛',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'chicken65',
        name: 'Chicken 65',
        description: 'Spicy deep-fried chicken with curry leaves and spices',
        price: 12.99,
        image: '🍗',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'paneer65',
        name: 'Paneer 65',
        description: 'Crispy paneer cubes in spicy masala coating',
        price: 10.99,
        image: '🧀',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      }
    ],
    mainDishes: [
      {
        id: 'butterChicken',
        name: 'Butter Chicken',
        description: 'Tender chicken in rich tomato and butter gravy',
        price: 18.99,
        image: '🍛',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'biryani',
        name: 'Biryani',
        description: 'Fragrant basmati rice with tender meat and aromatic spices',
        price: 22.99,
        image: '🍚',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'roganJosh',
        name: 'Rogan Josh',
        description: 'Tender lamb in aromatic Kashmiri spices',
        price: 24.99,
        image: '🥘',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'matarPaneer',
        name: 'Matar Paneer',
        description: 'Fresh paneer and green peas in spiced tomato gravy',
        price: 16.99,
        image: '🧀',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      }
    ],
    breads: [
      {
        id: 'naan',
        name: 'Naan',
        description: 'Soft leavened flatbread baked in tandoor',
        price: 3.99,
        image: '🫓',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'roti',
        name: 'Roti',
        description: 'Whole wheat flatbread cooked on griddle',
        price: 2.99,
        image: '🫓',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      }
    ],
    sides: [
      {
        id: 'rice',
        name: 'Basmati Rice',
        description: 'Fragrant long-grain rice, perfect with curries',
        price: 4.99,
        image: '🍚',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      },
      {
        id: 'potatoes',
        name: 'Spiced Potatoes',
        description: 'Crispy potatoes with aromatic Indian spices',
        price: 6.99,
        image: '🥔',
        video: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4'
      }
    ]
  };

  const categories = [
    { id: 'starters', name: 'Starters & Snacks', icon: '🥟' },
    { id: 'mainDishes', name: 'Main Dishes', icon: '🍛' },
    { id: 'breads', name: 'Breads', icon: '🫓' },
    { id: 'sides', name: 'Sides', icon: '🥗' }
  ];

  const handleAddToCart = (item) => {
    addToCart(item);
    toast.success(`${item.name} added to cart!`);
  };

  const MenuItem = ({ item }) => {
    const [isHovered, setIsHovered] = useState(false);

    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="card overflow-hidden"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        {/* Video Thumbnail */}
        <div className="relative h-48 bg-gray-200 overflow-hidden">
          {isHovered ? (
            <video
              autoPlay
              muted
              loop
              className="w-full h-full object-cover"
            >
              <source src={item.video} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          ) : (
            <div className="w-full h-full flex items-center justify-center text-6xl">
              {item.image}
            </div>
          )}
          <div className="absolute inset-0 bg-black/20"></div>
        </div>

        {/* Content */}
        <div className="p-6">
          <h3 className="text-xl font-bold text-gray-900 mb-2">{item.name}</h3>
          <p className="text-gray-600 mb-4">{item.description}</p>
          
          <div className="flex items-center justify-between">
            <span className="text-2xl font-bold text-primary-600">
              ${item.price}
            </span>
            <button
              onClick={() => handleAddToCart(item)}
              className="btn-primary flex items-center space-x-2"
            >
              <ShoppingCart className="h-4 w-4" />
              <span>Add to Cart</span>
            </button>
          </div>
        </div>
      </motion.div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 pt-20">
      <div className="container-custom section-padding">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 dark:text-white mb-6">
            Our <span className="text-gradient">Menu</span>
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Discover our authentic Indian dishes, carefully crafted with traditional 
            recipes and the finest ingredients to bring you the true taste of India.
          </p>
        </motion.div>

        {/* Category Tabs */}
        <div className="flex flex-wrap justify-center gap-4 mb-12">
          {categories.map((category) => (
            <button
              key={category.id}
              onClick={() => setActiveCategory(category.id)}
              className={`flex items-center space-x-2 px-6 py-3 rounded-full font-medium transition-all duration-300 ${
                activeCategory === category.id
                  ? 'bg-primary-500 text-white shadow-lg'
                  : 'bg-white text-gray-700 hover:bg-primary-50 hover:text-primary-600'
              }`}
            >
              <span className="text-xl">{category.icon}</span>
              <span>{category.name}</span>
            </button>
          ))}
        </div>

        {/* Menu Items */}
        <AnimatePresence mode="wait">
          <motion.div
            key={activeCategory}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.5 }}
            className="grid md:grid-cols-2 lg:grid-cols-3 gap-8"
          >
            {menuData[activeCategory].map((item) => (
              <MenuItem key={item.id} item={item} />
            ))}
          </motion.div>
        </AnimatePresence>

        {/* Special Offer */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="mt-20 text-center"
        >
          <div className="bg-gradient-to-r from-accent-500 to-accent-600 rounded-2xl p-8 text-white">
            <h3 className="text-3xl font-bold mb-4">
              🎉 Special Offer! 🎉
            </h3>
            <p className="text-xl mb-6">
              Order any main dish and get 20% off on starters!
            </p>
            <button className="btn-primary bg-white text-accent-600 hover:bg-gray-100">
              Order Now & Save
            </button>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default Menu;
