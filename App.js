import {StatusBar} from 'expo-status-bar';
import {StyleSheet, Text} from 'react-native';
import {SafeAreaProvider, SafeAreaView} from "react-native-safe-area-context";

export default function App() {
    return (
        <SafeAreaProvider style={styles.container}>
            <SafeAreaView>
                <Text>Open up App.js </Text>
                <StatusBar style="auto"/>
            </SafeAreaView>
        </SafeAreaProvider>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});
