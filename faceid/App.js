import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import RegistrationScreen from './Registration';
import { StatusBar } from 'expo-status-bar';
import { Amplify } from 'aws-amplify';
import awsmobile from './src/aws-exports';

Amplify.configure(awsmobile);

const Stack = createStackNavigator();
//use this to add more things like login screen, main screen, basically web pages like with html
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Registration" component={RegistrationScreen} />
        {}
      </Stack.Navigator>
      <StatusBar style="auto" />
    </NavigationContainer>
  );
}

export default App;
