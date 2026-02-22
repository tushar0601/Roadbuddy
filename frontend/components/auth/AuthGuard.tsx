"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabaseClient";
import { useAuth } from "@/lib/auth";

type Props = {
  children: React.ReactNode;
};

export function AuthGuard({ children }: Props) {
  const router = useRouter();
  const { setToken } = useAuth();

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function checkAuth() {
      const { data, error } = await supabase.auth.getSession();

      if (error || !data.session) {
        router.replace("/signin");
        return;
      }

      // keep your existing api.ts working
      setToken(data.session.access_token);

      setLoading(false);
    }

    checkAuth();
  }, [router, setToken]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Checking authentication...
      </div>
    );
  }

  return <>{children}</>;
}
