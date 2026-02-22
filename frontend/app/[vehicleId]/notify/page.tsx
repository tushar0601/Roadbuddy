"use client";

import { useParams } from "next/navigation";
import { useState } from "react";
import { API_BASE } from "@/lib/api";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

export default function NotifyPage() {
  const { vehicleId } = useParams<{ vehicleId: string }>();
  const [message, setMessage] = useState("Please move your vehicle.");
  const [done, setDone] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  async function notifyOwner() {
    setErr(null);
    const res = await fetch(`${API_BASE}/notification/vehicle/${vehicleId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!res.ok) {
      setErr(await res.text());
      return;
    }
    setDone(true);
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <Card className="w-full max-w-lg">
        <CardHeader>
          <CardTitle>Notify vehicle owner</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          {done ? (
            <div className="text-sm">✅ Owner has been notified.</div>
          ) : (
            <>
              <Textarea value={message} onChange={(e) => setMessage(e.target.value)} />
              <Button onClick={notifyOwner}>Notify owner</Button>
              {err && <div className="text-sm text-red-600">{err}</div>}
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
