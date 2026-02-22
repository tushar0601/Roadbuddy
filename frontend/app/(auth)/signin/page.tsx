/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabaseClient";
import { toast } from "sonner";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

function GoogleIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 533.5 544.3" aria-hidden="true" {...props}>
      <path
        d="M533.5 278.4c0-17.4-1.6-34.1-4.6-50.4H272v95.3h146.9c-6.3 34-25 62.8-53.3 82v68h86.2c50.4-46.4 81.7-114.9 81.7-194.9z"
        fill="currentColor"
        opacity="0.9"
      />
      <path
        d="M272 544.3c72.6 0 133.6-24.1 178.1-65.5l-86.2-68c-24 16.1-54.8 25.6-91.9 25.6-70.6 0-130.5-47.7-152-111.7H31.6v70.2C75.8 475.8 167 544.3 272 544.3z"
        fill="currentColor"
        opacity="0.75"
      />
      <path
        d="M120 324.7c-10.1-30-10.1-62.4 0-92.4V162H31.6c-37.2 74.2-37.2 161.9 0 236.1L120 324.7z"
        fill="currentColor"
        opacity="0.6"
      />
      <path
        d="M272 107.9c39.5-.6 77.6 14 106.6 40.9l79.4-79.4C410.9 24.5 343.2-1 272 0 167 0 75.8 68.5 31.6 162L120 232.3C141.5 155.6 201.4 107.9 272 107.9z"
        fill="currentColor"
        opacity="0.85"
      />
    </svg>
  );
}

export default function SignInPage() {
  const [loading, setLoading] = useState(false);

  async function signInWithGoogle() {
    setLoading(true);
    try {
      const redirectTo = `${window.location.origin}/auth/callback`;
      const { error } = await supabase.auth.signInWithOAuth({
        provider: "google",
        options: { redirectTo },
      });
      if (error) throw error;
      // Supabase redirects; no further action here.
    } catch (err: any) {
      toast.error(err?.message || "Google sign-in failed");
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-zinc-50 to-white dark:from-zinc-950 dark:to-black">
      <div className="mx-auto flex min-h-screen max-w-6xl items-center justify-center p-6">
        <div className="grid w-full items-stretch gap-6 md:grid-cols-2">
          {/* Left: Brand */}
          <div className="hidden md:flex flex-col justify-center rounded-2xl border bg-white/60 p-10 shadow-sm backdrop-blur dark:bg-zinc-950/40">
            <div className="space-y-4">
              <div className="inline-flex items-center gap-2">
                <div className="h-10 w-10 rounded-2xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-semibold">
                  RB
                </div>
                <div>
                  <div className="text-xl font-semibold">RoadBuddy</div>
                  <div className="text-sm text-muted-foreground">
                    QR-based parking pings — without sharing your phone number.
                  </div>
                </div>
              </div>

              <div className="space-y-2 text-sm text-muted-foreground">
                <div className="rounded-xl border bg-background p-4">
                  <div className="font-medium text-foreground">How it works</div>
                  <ul className="mt-2 list-disc space-y-1 pl-5">
                    <li>Add your vehicle</li>
                    <li>Generate a sticker QR</li>
                    <li>Someone scans → you get an in-app ping</li>
                  </ul>
                </div>

                <div className="rounded-xl border bg-background p-4">
                  <div className="font-medium text-foreground">Why it matters</div>
                  <p className="mt-2">
                    Privacy-first way to resolve “blocked vehicle” situations — safer for everyone.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Right: Sign in */}
          <Card className="rounded-2xl shadow-sm">
            <CardHeader className="space-y-2">
              <CardTitle className="text-2xl">Sign in</CardTitle>
              <CardDescription>
                Continue with Google to access your dashboard.
              </CardDescription>
            </CardHeader>

            <CardContent className="space-y-4">
              <Button
                className="w-full rounded-xl"
                size="lg"
                onClick={signInWithGoogle}
                disabled={loading}
              >
                <GoogleIcon className="mr-2 h-5 w-5" />
                {loading ? "Redirecting..." : "Continue with Google"}
              </Button>

              <div className="text-xs text-muted-foreground">
                By continuing, you agree to basic usage logging for abuse prevention (IP hash + user agent).
              </div>

              <div className="text-xs text-muted-foreground">
                Tip: If redirect fails, confirm your Supabase Auth settings allow{" "}
                <span className="font-medium text-foreground">/auth/callback</span> as a redirect URL.
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
