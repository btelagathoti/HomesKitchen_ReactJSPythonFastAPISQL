import React from 'react';
import { motion } from 'framer-motion';
import { Heart, Award, Users, Clock, Star, ChefHat, Leaf, Shield } from 'lucide-react';

const About = () => {
  const values = [
    {
      icon: <Heart className="h-8 w-8 text-red-500" />,
      title: "Passion for Food",
      description: "Every dish is prepared with love and dedication to authentic flavors"
    },
    {
      icon: <Leaf className="h-8 w-8 text-green-500" />,
      title: "Fresh Ingredients",
      description: "We source only the finest, freshest ingredients for our dishes"
    },
    {
      icon: <Shield className="h-8 w-8 text-blue-500" />,
      title: "Quality Assurance",
      description: "Maintaining the highest standards in food safety and preparation"
    },
    {
      icon: <Users className="h-8 w-8 text-purple-500" />,
      title: "Community Focus",
      description: "Building lasting relationships with our customers and community"
    }
  ];

  const milestones = [
    {
      year: "2010",
      title: "Restaurant Founded",
      description: "Started as a small family restaurant with a dream to share authentic Indian cuisine"
    },
    {
      year: "2015",
      title: "First Expansion",
      description: "Moved to a larger location and added delivery services"
    },
    {
      year: "2018",
      title: "Award Recognition",
      description: "Received 'Best Indian Restaurant' award from local food critics"
    },
    {
      year: "2023",
      title: "Digital Transformation",
      description: "Launched online ordering system and expanded menu offerings"
    }
  ];

  const teamMembers = [
    {
      name: "Raj Patel",
      role: "Head Chef & Owner",
      image: "👨‍🍳",
      description: "With over 20 years of experience, Raj brings traditional family recipes to life"
    },
    {
      name: "Priya Sharma",
      role: "Sous Chef",
      image: "👩‍🍳",
      description: "Specializes in North Indian cuisine and bread making"
    },
    {
      name: "Amit Kumar",
      role: "Restaurant Manager",
      image: "👨‍💼",
      description: "Ensures every customer has an exceptional dining experience"
    },
    {
      name: "Sofia Rodriguez",
      role: "Service Lead",
      image: "👩‍💼",
      description: "Creates warm, welcoming atmosphere for all guests"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 pt-20">
      <div className="container-custom section-padding">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            About <span className="text-gradient">Home' Kitchen</span>
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Discover the story behind our passion for authentic Indian cuisine and 
            the family traditions that make every meal special.
          </p>
        </motion.div>

        {/* Our Story */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-bold text-gray-900 mb-6">Our Story</h2>
              <div className="space-y-4 text-lg text-gray-600">
                <p>
                  Founded in 2010 by the Patel family, Home' Kitchen began as a humble 
                  dream to share the authentic flavors of India with our community. 
                  What started in a small kitchen has grown into a beloved destination 
                  for food lovers seeking genuine Indian cuisine.
                </p>
                <p>
                  Our journey is rooted in family traditions passed down through 
                  generations. Every recipe tells a story, every spice has a purpose, 
                  and every dish is prepared with the same love and care that our 
                  grandmothers put into their cooking.
                </p>
                <p>
                  Today, we continue to honor these traditions while embracing 
                  modern culinary techniques and sustainable practices. Our commitment 
                  to quality, authenticity, and community remains at the heart of 
                  everything we do.
                </p>
              </div>
            </div>
            <div className="relative">
              <div className="aspect-square bg-gradient-to-br from-primary-100 to-accent-100 rounded-2xl flex items-center justify-center">
                <ChefHat className="h-32 w-32 text-primary-500" />
              </div>
              <div className="absolute -bottom-6 -right-6 bg-white rounded-xl p-4 shadow-lg">
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary-600">13+</div>
                  <div className="text-sm text-gray-600">Years of Excellence</div>
                </div>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Our Values */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Our Values</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              The principles that guide everything we do at Home' Kitchen
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {values.map((value, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                className="card p-6 text-center"
              >
                <div className="mb-4 flex justify-center">
                  {value.icon}
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">
                  {value.title}
                </h3>
                <p className="text-gray-600">
                  {value.description}
                </p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Milestones */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Our Journey</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Key milestones that shaped our restaurant's growth and success
            </p>
          </div>

          <div className="relative">
            {/* Timeline Line */}
            <div className="absolute left-1/2 transform -translate-x-1/2 w-1 bg-primary-200 h-full"></div>
            
            <div className="space-y-12">
              {milestones.map((milestone, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  className={`flex items-center ${index % 2 === 0 ? 'flex-row' : 'flex-row-reverse'}`}
                >
                  <div className={`w-1/2 ${index % 2 === 0 ? 'pr-8 text-right' : 'pl-8 text-left'}`}>
                    <div className="card p-6">
                      <div className="text-3xl font-bold text-primary-600 mb-2">
                        {milestone.year}
                      </div>
                      <h3 className="text-xl font-bold text-gray-900 mb-2">
                        {milestone.title}
                      </h3>
                      <p className="text-gray-600">
                        {milestone.description}
                      </p>
                    </div>
                  </div>
                  
                  {/* Timeline Dot */}
                  <div className="relative z-10">
                    <div className="w-4 h-4 bg-primary-500 rounded-full border-4 border-white shadow-lg"></div>
                  </div>
                  
                  <div className="w-1/2"></div>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.div>

        {/* Our Team */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Meet Our Team</h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              The passionate individuals who make Home' Kitchen a special place
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {teamMembers.map((member, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                className="card p-6 text-center"
              >
                <div className="text-6xl mb-4">{member.image}</div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">
                  {member.name}
                </h3>
                <div className="text-primary-600 font-medium mb-3">
                  {member.role}
                </div>
                <p className="text-gray-600 text-sm">
                  {member.description}
                </p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Awards & Recognition */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center"
        >
          <div className="card p-8 bg-gradient-to-r from-primary-600 to-primary-800 text-white">
            <h2 className="text-4xl font-bold mb-6">Awards & Recognition</h2>
            <div className="grid md:grid-cols-3 gap-8">
              <div className="flex items-center justify-center space-x-3">
                <Award className="h-8 w-8 text-accent-400" />
                <span className="text-lg">Best Indian Restaurant 2018</span>
              </div>
              <div className="flex items-center justify-center space-x-3">
                <Star className="h-8 w-8 text-accent-400" />
                <span className="text-lg">4.8/5 Customer Rating</span>
              </div>
              <div className="flex items-center justify-center space-x-3">
                <Clock className="h-8 w-8 text-accent-400" />
                <span className="text-lg">13+ Years of Service</span>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default About;
