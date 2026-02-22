import "./globals.css";
import { AuthProvider } from "@/lib/auth";
import { Toaster } from "@/components/ui/sonner";
import { AuthSync } from "@/components/auth/AuthSync";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <AuthSync />
          {children}
          <Toaster />
        </AuthProvider>
      </body>
    </html>
  );
}
