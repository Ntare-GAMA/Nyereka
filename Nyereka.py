import React, { useState } from 'react';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { AlertCircle, CheckCircle, ShieldAlert } from 'lucide-react';

const NyerekaSecurityChecker = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [securityResults, setSecurityResults] = useState(null);
  const [error, setError] = useState(null);

  // Simulated Security Check Function
  const checkNyerekaSecurity = async (email) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        // Simulated security check results
        const securityIssues = [
          {
            type: 'UnverifiedDevice',
            description: 'Unrecognized device detected on your account',
            severity: 'medium'
          },
          {
            type: 'RecentUnusualActivity',
            description: 'Suspicious login from an unexpected location',
            severity: 'high'
          }
        ];

        // Randomize results for demonstration
        const hasIssues = Math.random() > 0.5;

        resolve({
          email,
          hasSecurityIssues: hasIssues,
          issues: hasIssues ? securityIssues : [],
          recommendedActions: [
            'Update your account password',
            'Enable two-factor authentication',
            'Review recent account activity'
          ]
        });
      }, 1500);
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Please enter a valid email address');
      return;
    }

    setLoading(true);
    setError(null);
    setSecurityResults(null);

    try {
      const results = await checkNyerekaSecurity(email);
      setSecurityResults(results);
    } catch (err) {
      setError('Failed to check security. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="flex items-center">
            <ShieldAlert className="mr-2" /> Nyereka Security Checker
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input 
              type="email" 
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full"
            />
            <Button 
              type="submit" 
              className="w-full" 
              disabled={loading}
            >
              {loading ? 'Checking Security...' : 'Check Security'}
            </Button>

            {error && (
              <Alert variant="destructive">
                <AlertCircle className="h-4 w-4" />
                <AlertTitle>Error</AlertTitle>
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            {loading && (
              <div className="text-center text-gray-500">
                Analyzing your account security...
              </div>
            )}

            {securityResults && !loading && (
              <div>
                {securityResults.hasSecurityIssues ? (
                  <Alert variant="destructive">
                    <AlertCircle className="h-4 w-4" />
                    <AlertTitle>Security Concerns Detected!</AlertTitle>
                    <AlertDescription>
                      Potential security issues found for {securityResults.email}
                      <ul className="mt-2 list-disc pl-5">
                        {securityResults.issues.map((issue, index) => (
                          <li key={index} className="mb-1">
                            <strong>{issue.type}</strong>: {issue.description}
                            <span className="ml-2 text-sm text-red-600">
                              (Severity: {issue.severity})
                            </span>
                          </li>
                        ))}
                      </ul>
                      <div className="mt-3">
                        <strong>Recommended Actions:</strong>
                        <ul className="list-disc pl-5">
                          {securityResults.recommendedActions.map((action, index) => (
                            <li key={index}>{action}</li>
                          ))}
                        </ul>
                      </div>
                    </AlertDescription>
                  </Alert>
                ) : (
                  <Alert variant="default">
                    <CheckCircle className="h-4 w-4 text-green-500" />
                    <AlertTitle>No Major Security Issues</AlertTitle>
                    <AlertDescription>
                      Your account appears to be secure. 
                      Continue to follow best practices for online safety.
                    </AlertDescription>
                  </Alert>
                )}
              </div>
            )}
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default NyerekaSecurityChecker;
