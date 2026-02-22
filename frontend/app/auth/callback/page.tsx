"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabaseClient";
import { useAuth } from "@/lib/auth";
import { toast } from "sonner";

export default function AuthCallbackPage() {
  const router = useRouter();
  const { setToken } = useAuth();

  useEffect(() => {
    (async () => {
      // After OAuth redirect, Supabase should already have persisted the session.
      const { data, error } = await supabase.auth.getSession();

      if (error) {
        toast.error(error.message);
        router.replace("/signin");
        return;
      }

      const accessToken = data.session?.access_token;
      if (!accessToken) {
        toast.error("No session found. Please sign in again.");
        router.replace("/signin");
        return;
      }

      // This makes your existing api.ts keep working (Bearer token).
      setToken(accessToken);

      toast.success("Signed in");
      router.replace("/dashboard");
    })();
  }, [router, setToken]);

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <div className="text-sm text-muted-foreground">Signing you in…</div>
    </div>
  );
}
