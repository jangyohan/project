import React, { Component } from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
} from 'react-native';

export default class HomeButton extends Component{
    static defaultProps = {
      title: '컴알못',
      buttonColor: '#363636',
      titleColor: '#fff',
      onPress: () => null,
    }
    constructor(props){
        super(props);
      }
      render(){
        return (
          <TouchableOpacity style={[
            styles.button,
            {backgroundColor: this.props.buttonColor}
          ]}
          onPress={this.props.onPress}>
            <Text style={[
              styles.title,
              {color: this.props.titleColor}
            ]}>{this.props.title}</Text>
          </TouchableOpacity>
        )
      }
    }
    const styles = StyleSheet.create({
        button: {
          flex: 1,
          alignItems: 'center',
          justifyContent: 'center',
          marginBottom: 10,
        },
        title: {
          fontSize: 15,
        },
      });