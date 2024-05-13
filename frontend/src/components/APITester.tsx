import axios from 'axios';
import { useState } from 'react';

const APITester = () => {
    const [response, setResponse] = useState<string>('');
  
    const testAPIConnection = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/ai/test');
        setResponse('Success: ' + res.data.message);
      } catch (error: any) {
        setResponse('Error: ' + error.message);
      }
    };
  
    return (
      <div>
        <button className='APITester' onClick={testAPIConnection}>Test API Connection</button>
        <p>{response}</p>
      </div>
    );
  };
  
  export default APITester;