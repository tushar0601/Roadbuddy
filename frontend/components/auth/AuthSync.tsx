"use client";

import { useEffect } from "react";
import { supabase } from "@/lib/supabaseClient";
import { useAuth } from "@/lib/auth";

export function AuthSync() {
  const { setToken } = useAuth();

  useEffect(() => {
    const { data: sub } = supabase.auth.onAuthStateChange((_event, session) => {
      setToken(session?.access_token ?? null);
    });

    return () => {
      sub.subscription.unsubscribe();
    };
  }, [setToken]);

  return null;
}
