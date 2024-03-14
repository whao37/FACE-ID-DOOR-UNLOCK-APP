import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet, Text } from 'react-native';
import switchScreen from './App';

const HomeScreen = ({ navigation }) => {

  const handleDevice = () => {
    //need to get devices from backend
    switchScreen(HomeScreen, "Home");
    alert('device selected');
  };

  return (
    <View style={styles.container}>
      
      <Button title="Device" onPress={handleDevice} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    padding: 10,
  },
});
export default HomeScreen;
