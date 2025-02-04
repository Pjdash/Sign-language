import React, { useState, useEffect } from 'react';
import { Hand, Volume2, VolumeX, RefreshCw, Info } from 'lucide-react';
import { io } from "socket.io-client";

// Connect to the WebSocket server
const socket = io("http://localhost:5000");

function App() {
  const [predictedLetter, setPredictedLetter] = useState<string>('A');
  const [confidence, setConfidence] = useState<number>(95);
  const [isVoiceEnabled, setIsVoiceEnabled] = useState<boolean>(true);
  const [isDetecting, setIsDetecting] = useState<boolean>(true);

  // Simulate predictions (replace with actual device integration)
  useEffect(() => {
    const interval = setInterval(() => {
      const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      const randomLetter = letters[Math.floor(Math.random() * letters.length)];
      const randomConfidence = 85 + Math.random() * 15;
      setPredictedLetter(randomLetter);
      setConfidence(randomConfidence);

      // Speak the letter if voice is enabled
      if (isVoiceEnabled) {
        const utterance = new SpeechSynthesisUtterance(`Letter ${randomLetter}`);
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        window.speechSynthesis.speak(utterance);
      }
    }, 3000);

    return () => clearInterval(interval);
  }, [isVoiceEnabled]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 p-6">
      <div className="max-w-md mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div className="flex items-center gap-2">
            <Hand className="w-8 h-8 text-indigo-600" />
            <h1 className="text-2xl font-bold text-gray-800">Sign Language Recogniser</h1>
          </div>
          <button 
            onClick={() => setIsVoiceEnabled(prev => !prev)}
            className="p-2 rounded-full bg-white shadow-sm hover:bg-gray-50 transition-colors"
            aria-label={isVoiceEnabled ? "Disable voice" : "Enable voice"}
          >
            {isVoiceEnabled ? (
              <Volume2 className="w-6 h-6 text-green-600" />
            ) : (
              <VolumeX className="w-6 h-6 text-gray-400" />
            )}
          </button>
        </div>

        {/* Main Display */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="text-center">
            <div className="relative inline-block">
              <div className="text-9xl font-bold text-indigo-600 mb-4">
                {predictedLetter}
              </div>
              {isDetecting && (
                <RefreshCw className="w-6 h-6 text-indigo-400 animate-spin absolute top-0 right-0" />
              )}
            </div>
            <div className="text-gray-500 mb-6">Predicted Letter</div>
          </div>

          {/* Confidence Bar */}
          <div className="space-y-2">
            <div className="flex justify-between text-sm text-gray-600">
              <span>Confidence</span>
              <span>{confidence.toFixed(1)}%</span>
            </div>
            <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
              <div 
                className="h-full bg-indigo-600 rounded-full transition-all duration-300"
                style={{ width: `${confidence}%` }}
              />
            </div>
          </div>
        </div>

        {/* Instructions */}
        <div className="bg-white rounded-xl shadow-sm p-4">
          <div className="flex items-start gap-3">
            <Info className="w-5 h-5 text-indigo-600 mt-0.5" />
            <div>
              <h3 className="font-medium text-gray-800 mb-1">Tips for Best Results</h3>
              <ul className="text-sm text-gray-600 space-y-1">
                <li>• Keep your hand  stable for a while </li>
                <li>• Ensure   that the  glove is  worn  properly </li>
                <li>• Hold each sign steady for 1-2 seconds</li>
                <li>• Toggle voice assistant using the speaker icon</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;